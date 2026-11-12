---
title: "CenteredOnBendLines Property (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "CenteredOnBendLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~CenteredOnBendLines.html"
---

# CenteredOnBendLines Property (IBreakCornerFeatureData)

Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CenteredOnBendLines As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim value As System.Boolean

instance.CenteredOnBendLines = value

value = instance.CenteredOnBendLines
```

### C#

```csharp
System.bool CenteredOnBendLines {get; set;}
```

### C++/CLI

```cpp
property System.bool CenteredOnBendLines {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to center the corner cuts on the bend lines, false to not

## VBA Syntax

See [BreakCornerFeatureData::CenteredOnBendLines](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~CenteredOnBendLines.html).

## Examples

[Modify Break Corner Feature (C#)](Modify_Break_Corner_Feature_Example_CSharp.htm)
[Modify Break Corner Feature (VB.NET)](Modify_Break_Corner_Feature_Example_VBNET.htm)
[Modify Break Corner Feature (VBA)](Modify_Break_Corner_Feature_Example_VB.htm)

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
