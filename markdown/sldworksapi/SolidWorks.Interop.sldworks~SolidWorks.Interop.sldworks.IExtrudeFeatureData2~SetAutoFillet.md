---
title: "SetAutoFillet Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetAutoFillet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetAutoFillet.html"
---

# SetAutoFillet Method (IExtrudeFeatureData2)

Sets the automatic corner fillet properties of this thin feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAutoFillet( _
   ByVal AutoFillet As System.Boolean, _
   ByVal Radius As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim AutoFillet As System.Boolean
Dim Radius As System.Double
Dim value As System.Boolean

value = instance.SetAutoFillet(AutoFillet, Radius)
```

### C#

```csharp
System.bool SetAutoFillet(
   System.bool AutoFillet,
   System.double Radius
)
```

### C++/CLI

```cpp
System.bool SetAutoFillet(
   System.bool AutoFillet,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AutoFillet`: True to fillet the corners automatically, false to not
- `Radius`: Fillet radius, if automatic corner fillets is enabled

### Return Value

True if the corners are automatically filleted, false if not

## VBA Syntax

See [ExtrudeFeatureData2::SetAutoFillet](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetAutoFillet.html).

## Remarks

This method only applies to thin feature extrusions. If the feature is not a thin feature extrusion, then no action is taken and the COM version of this method returns S_false in the status return value.

If disabling the automatic corner fillets property (AutoFillet = false), then the Radius value is not used.

To get the automatic corner fillet flag, use [IExtrudeFeatureData2::GetAutoFilletCorners](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletCorners.html). To get the fillet radius, use [IExtrudeFeatureData2::GetAutoFilletRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletRadius.html) .

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.html)

## Availability

SOLIDWORKS 2004 SP5, Revision Number 12.5
