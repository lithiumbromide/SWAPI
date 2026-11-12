---
title: "Thickness Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "Thickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~Thickness.html"
---

# Thickness Property (ISheetMetalFeatureData)

Gets or sets the sheet metal thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property Thickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Double

instance.Thickness = value

value = instance.Thickness
```

### C#

```csharp
System.double Thickness {get; set;}
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the thickness

## VBA Syntax

See [SheetMetalFeatureData::Thickness](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~Thickness.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
