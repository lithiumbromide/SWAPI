---
title: "Other Microsoft VBA-enabled Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Other_Microsoft_VBA-enabled_Applications.htm"
---

# Other Microsoft VBA-enabled Applications

Because Microsoft VBA is embedded in SOLIDWORKS, SOLIDWORKS can inter-operate with other VBA-enabled applications, such as Microsoft Excel, Microsoft Access, and Microsoft Visio.

For example, you can create a VBA application in SOLIDWORKS that attaches to a running instance of Microsoft Excel. You can then access the active sheet and retrieve data to use with SOLIDWORKS.

The following code shows how to attach to the active Microsoft Excel object, get the value in cell A1 in the active sheet, and use that value to set the density in a SOLIDWORKS part.

```vb
' Attach to active Excel object
Set xl = GetObject(, "Excel.Application")
' Get active sheet in Excel
Set xlsh = xl.ActiveSheet
' Get value in Excel cell A1
density = xlsh.Cells(1,1)
' Set density in SOLIDWORKS part
Part.SetUserPreferenceDoubleValue swMaterialPropertyDensity, density
```

Alternatively you can also attach to a running instance of SOLIDWORKS from a VBA application created in Microsoft Excel.

In general, if your application is primarily a SOLIDWORKS API application, then develop the application in SOLIDWORKS .
