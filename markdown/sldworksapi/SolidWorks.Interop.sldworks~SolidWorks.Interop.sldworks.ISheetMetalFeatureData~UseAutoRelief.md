---
title: "UseAutoRelief Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "UseAutoRelief"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseAutoRelief.html"
---

# UseAutoRelief Property (ISheetMetalFeatureData)

Gets or sets whether this sheet metal feature uses auto relief.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseAutoRelief As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Boolean

instance.UseAutoRelief = value

value = instance.UseAutoRelief
```

### C#

```csharp
System.bool UseAutoRelief {get; set;}
```

### C++/CLI

```cpp
property System.bool UseAutoRelief {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use auto relief, false to not

## VBA Syntax

See [SheetMetalFeatureData::UseAutoRelief](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~UseAutoRelief.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
[ISheetMetalFeatureData::AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AutoReliefType.html)
[ISheetMetalFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~ReliefRatio.html)

## Availability

SOLIDWORKS 2001 Sp1, Revision Number 9.1
