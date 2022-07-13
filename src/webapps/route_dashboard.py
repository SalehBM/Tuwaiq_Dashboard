# ######################### #
#     Tuwaiq Dashboard      #
#      Dashboard Page       #
# ######################### #

from fastapi import APIRouter, Request, Depends
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar

from routers.admin import get_all_admin, get_users_year
from routers.course import get_all_courses, get_last_three_months
from routers.submission import get_all_submissions, get_all_submissions_year
from routers.attendance import get_attendances_today
from db.repository.login import get_current_user_from_token
from db.models.AdminUser import AdminUser
from webapps.base import templates

router = APIRouter(include_in_schema=False)

def getLast_12_months():
    return [calendar.month_abbr[(date.today() - relativedelta(months=n)).month] for n in range(11, -1, -1)]

def constMonth():
    return f"const months = {str(getLast_12_months())}"

def getBarChart(months):
    return """
    const barChart = new Chart(document.getElementById('barChart'), {
  type: 'bar',
  data: {
    labels: months,
    datasets: [
      {
        data: """ + str(months) + """,
        backgroundColor: colors.primary,
        hoverBackgroundColor: colors.primaryDark,
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          gridLines: false,
          ticks: {
            beginAtZero: true,
            stepSize: 50,
            fontSize: 12,
            fontColor: '#97a4af',
            fontFamily: 'Open Sans, sans-serif',
            padding: 10,
          },
        },
      ],
      xAxes: [
        {
          gridLines: false,
          ticks: {
            fontSize: 12,
            fontColor: '#97a4af',
            fontFamily: 'Open Sans, sans-serif',
            padding: 5,
          },
          categoryPercentage: 0.5,
          maxBarThickness: '10',
        },
      ],
    },
    cornerRadius: 2,
    maintainAspectRatio: false,
    legend: {
      display: false,
    },
  },
})
    """

def getDoughnutChart(months: dict):
    return """
    const doughnutChart = new Chart(document.getElementById('doughnutChart'), {
  type: 'doughnut',
  data: {
    labels: """ + str([x for x in months.keys()]) +""",
    datasets: [
      {
        data: """ + str([x for x in months.values()]) + """,
        backgroundColor: [colors.primary, colors.primaryLighter, colors.primaryLight],
        hoverBackgroundColor: colors.primaryDark,
        borderWidth: 0,
        weight: 0.5,
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    legend: {
      position: 'bottom',
    },

    title: {
      display: false,
    },
    animation: {
      animateScale: true,
      animateRotate: true,
    },
  },
})
    """

def getLineChart():
    return """
    const lineChart = new Chart(document.getElementById('lineChart'), {
  type: 'line',
  data: {
    labels: months,
    datasets: [
      {
        data: """ + str(get_users_year()) + """,
        fill: false,
        borderColor: colors.primary,
        borderWidth: 2,
        pointRadius: 0,
        pointHoverRadius: 0,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      yAxes: [
        {
          gridLines: false,
          ticks: {
            beginAtZero: false,
            stepSize: 50,
            fontSize: 12,
            fontColor: '#97a4af',
            fontFamily: 'Open Sans, sans-serif',
            padding: 20,
          },
        },
      ],
      xAxes: [
        {
          gridLines: false,
        },
      ],
    },
    maintainAspectRatio: false,
    legend: {
      display: false,
    },
    tooltips: {
      hasIndicator: true,
      intersect: false,
    },
  },
})
    """

def getAttedanceChart():
    return """
    const activeUsersChart = new Chart(document.getElementById('activeUsersChart'), {
  type: 'bar',
  data: {
    labels: ["", "", "", "", "", "", "", "", "", "", ""],
    datasets: [
      {
        data: [1, 5, 10, 20, 30, 40, 45, 48, 35, 25, 47],
        backgroundColor: colors.primary,
        borderWidth: 0,
        categoryPercentage: 1,
      },
    ],
  },
  options: {
    scales: {
      yAxes: [
        {
          display: false,
          gridLines: false,
        },
      ],
      xAxes: [
        {
          display: false,
          gridLines: false,
        },
      ],
      ticks: {
        padding: 10,
      },
    },
    cornerRadius: 2,
    maintainAspectRatio: false,
    legend: {
      display: false,
    },
    tooltips: {
      prefix: 'Users',
      bodySpacing: 4,
      footerSpacing: 4,
      hasIndicator: true,
      mode: 'index',
      intersect: true,
    },
    hover: {
      mode: 'nearest',
      intersect: true,
    },
  },
})

const usersCount = document.getElementById('usersCount')

const AttedancesUpdate = () => {
  UserCount = """ + str(len(get_attendances_today())) + """
  activeUsersChart.data.datasets[0].data.push(UserCount)
  activeUsersChart.data.datasets[0].data.splice(0, 1)
  activeUsersChart.update()
  usersCount.innerText = UserCount
}

setInterval(() => {
  AttedancesUpdate()
}, 1000)

    """

@router.get("/dashboard")
async def dashboard(request:Request, auth: AdminUser = Depends(get_current_user_from_token)):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "users_count": len(get_all_admin()),
        "courses_count": len(get_all_courses()),
        "submissions_count": len(get_all_submissions()),
        "attendance_count": len(get_attendances_today()),
        "charts": f"<script> {constMonth()}\n {getBarChart(get_all_submissions_year())}\n{getDoughnutChart(get_last_three_months())}\n{getLineChart()}\n{getAttedanceChart()}</script>"
        })
