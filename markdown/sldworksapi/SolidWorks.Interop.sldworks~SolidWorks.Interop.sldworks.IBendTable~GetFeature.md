---
title: "GetFeature Method (IBendTable)"
project: "SOLIDWORKS API Help"
interface: "IBendTable"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetFeature.html"
---

# GetFeature Method (IBendTable)

Gets the feature for this bend table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IBendTable
Dim value As Feature

value = instance.GetFeature()
```

### C#

```csharp
Feature GetFeature()
```

### C++/CLI

```cpp
Feature^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [BendTable::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~BendTable~GetFeature.html).

## Examples

[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)
[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)

## See Also

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
