#!/usr/bin/env python3

import meraki
import csv

API_KEY = ""
dashboard = meraki.DashboardAPI(API_KEY)
organizations = dashboard.organizations.getOrganizations()


def merakiunclaim(dashboard):
    print(organizations)
    with open('unclaim.csv', 'r', newline='') as csvfile:
        readfile = csv.reader(csvfile)
        snlist = list(readfile)
    print(snlist)
    dashboard.organizations.releaseFromOrganizationInventory(organizations[0]['id'], serials=snlist)


if __name__ == '__main__':
    merakiunclaim(dashboard)
