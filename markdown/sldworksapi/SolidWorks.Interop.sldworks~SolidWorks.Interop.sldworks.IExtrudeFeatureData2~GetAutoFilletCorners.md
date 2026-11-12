---
title: "GetAutoFilletCorners Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetAutoFilletCorners"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletCorners.html"
---

# GetAutoFilletCorners Method (IExtrudeFeatureData2)

Gets whether the corners of this thin feature are automatically filleted.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoFilletCorners() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

value = instance.GetAutoFilletCorners()
```

### C#

```csharp
System.bool GetAutoFilletCorners()
```

### C++/CLI

```cpp
System.bool GetAutoFilletCorners();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the corners are automatically filleted, false if not

## VBA Syntax

See [ExtrudeFeatureData2::GetAutoFilletCorners](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetAutoFilletCorners.html).

## Remarks

This method only applies to thin feature extrusions. If the feature is not a thin feature extrusion, then the return value is false, and the COM version of this method returns S_false in the status return value.

To get the fillet radius, use [IExtrudeFeatureData2::GetAutoFilletRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletRadius.html). To set automatic fillets and radius, use [IExtrudeFeatureData2::SetAutoFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetAutoFillet.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)

## Availability

SOLIDWORKS 2004 SP5, Revision Number 12.5
