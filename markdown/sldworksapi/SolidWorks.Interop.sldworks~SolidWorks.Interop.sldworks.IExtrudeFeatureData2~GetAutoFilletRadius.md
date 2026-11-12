---
title: "GetAutoFilletRadius Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetAutoFilletRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletRadius.html"
---

# GetAutoFilletRadius Method (IExtrudeFeatureData2)

Gets the automatic corner fillet radius for this thin feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoFilletRadius() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Double

value = instance.GetAutoFilletRadius()
```

### C#

```csharp
System.double GetAutoFilletRadius()
```

### C++/CLI

```cpp
System.double GetAutoFilletRadius();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Fillet radius, if feature has automatic corner fillets enabled

## VBA Syntax

See [ExtrudeFeatureData2::GetAutoFilletRadius](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetAutoFilletRadius.html).

## Remarks

This method only applies to thin feature extrusions. If the feature is not a thin feature extrusion, then the return value is 0.0, and the COM version of this method returns S_false in the status return value.

If the feature does not have automatic corner fillets enabled, then the return value is 0.0 and the COM version of this method returns S_false in the status return value.

To get whether automatic corner fillet is enabled, use [IExtrudeFeatureData2::GetAutoFilletCorners](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletCorners.html). To set automatic fillets and radius, use [IExtrudeFeatureData2::SetAutoFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetAutoFillet.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)

## Availability

SOLIDWORKS 2004 SP5, Revision Number 12.5
