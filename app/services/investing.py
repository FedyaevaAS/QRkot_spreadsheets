from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def get_project(session: AsyncSession):
    charity_projects = await session.execute(
        select(CharityProject).where(
            CharityProject.fully_invested == 0
        ).order_by('create_date')
    )
    project = charity_projects.scalars().first()
    return project


async def get_donation(session: AsyncSession):
    donations = await session.execute(
        select(Donation).where(
            Donation.fully_invested == 0
        ).order_by('create_date')
    )
    donation = donations.scalars().first()
    return donation


async def investing_process(first_obj, second_obj, amount=0, equal=False):
    first_obj.invested_amount = first_obj.full_amount
    first_obj.fully_invested = True
    first_obj.close_date = datetime.now()
    second_obj.invested_amount += amount
    if equal is True:
        await investing_process(second_obj, first_obj, equal=False)


async def investing(
    session: AsyncSession,
    obj
):
    project = await get_project(session)
    donation = await get_donation(session)
    if not project or not donation:
        await session.commit()
        await session.refresh(obj)
        return obj
    donation_amount = donation.full_amount - donation.invested_amount
    need_to_donate = project.full_amount - project.invested_amount
    if donation_amount > need_to_donate:
        await investing_process(project, donation, need_to_donate)
    elif donation_amount == need_to_donate:
        await investing_process(project, donation, equal=True)
    else:
        await investing_process(donation, project, donation_amount)
    session.add(project)
    session.add(donation)
    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    return await investing(session, obj)
