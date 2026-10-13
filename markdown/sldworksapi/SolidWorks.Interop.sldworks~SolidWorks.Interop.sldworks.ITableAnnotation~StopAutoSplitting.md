---
title: "StopAutoSplitting Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "StopAutoSplitting"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting.html"
---

# StopAutoSplitting Property (ITableAnnotation)

Stops the automatic horizontal splitting of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property StopAutoSplitting As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Boolean

instance.StopAutoSplitting = value

value = instance.StopAutoSplitting
```

### C#

```csharp
System.bool StopAutoSplitting {get; set;}
```

### C++/CLI

```cpp
property System.bool StopAutoSplitting {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to stop the automatic horizontal splitting of this table, false to not

## VBA Syntax

See [TableAnnotation::StopAutoSplitting](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~StopAutoSplitting.html).

## Remarks

This property works with [ITableAnnotation::HorizontalAutoSplit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.html) to control the automatic horizontal splitting of:

- [Hole tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html)
- [Bill of Materials tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html)
- [General tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableAnnotation.html)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::Split Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html)
[ITableAnnotation::GetSplitInformation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
