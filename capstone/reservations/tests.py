import pytest
from diy_users.models import DIYUsers

from hunter_diy_garage.models import AutoBay

from .models import Reservation
from django.utils import timezone
# Create your tests here.


@pytest.mark.django_db
def test_reservation_create():

    reservation = Reservation()
    # reservation.save(force_insert=False, force_update=False)
    auto_bay_id=AutoBay()
    diy_user_id=DIYUsers()

    reservation = Reservation.objects.create(
        electricity_used=3.25,
        hours_used=5.4,
        auto_bay_id=2,
        diy_user_id="user11",
        date_reserved=timezone.now(),
        reservation_date=timezone.activate("America/New_York"),
        time_limit=4,
    )

    assert reservation.time_limit == 4
    assert reservation.electricity_used == 3.25
