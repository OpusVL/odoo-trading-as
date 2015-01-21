# odoo-trading-as
Module to allow printing of alternative letter heads for certain trading brands, without full multicompany
trading.

Work in progress - the data model is in a state of flux while we resolve interface compatibility
between our trading as model and res.company.

## trading\_as

Implements alternative company branding on all reports.

### How to create a brand

Under the company which needs the new brand option:

```
Settings -> Companies -> Your Company
```

You should see a new tab 'Brands'.

Click Edit, and then Brands.

Click 'Add new item' in the Brands list.

Choose 'Your Company' for 'legal entity'.

Under the Partners list, click Create and Edit.

Fill in the name and address details of the partner and click Save.

Enter the tagline and the footer to print on the reports.

Click the logo to the left of the Brand Name and pick an appropriately-sized
version of your brand's logo.

Click Save.

Click Save on the company object.

### How to apply a brand

When creating or editing a customer, there is a field 'Trader' which you can set
to one of the brands.  If it's blank, then all reports for this customer will just take
the company branding.  If it's set to a brand, then that brand is used.

### How brand is decided

The report for any object that has a 'partner\_id' will check if 'partner\_id.trader'
is set.  If it is, then it will use that trader object for the header and footer.
Otherwise, it will use the partner's company or the current user's company according
to the usual Odoo logic.

### Known Limitations

* You currently have to select the legal entity during creation of
  a brand - it doesn't default to the company from which it's being created.

* You have to create the partner explicitly.  res.company does somehow create its
  partner\_id delegate object automatically, but time constraints mean emulating res.company in that way
  is out of scope at the moment.

* The data links are in place for supporting multicompany (i.e. brands are attached to companies)
  but there's no logic for validation etc that would be needed in a multicompany setting,
  so the first time we need to use this in a multicompany setting some work will be needed to
  make sure all that works, specifically that only brands under the user's or partner's company
  are exposed.  Precisely what the logic should be is not yet decided.

# Copyright and License

Copyright (C) 2015 OpusVL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

If you require assistance, support, or further development of this
software, please contact OpusVL using the details below:

* Telephone: +44 (0)1788 298 410
* Email: community@opusvl.com
* Web: http://opusvl.com

