---
title: "ICreateBoundedSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateBoundedSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBoundedSurface.html"
---

# ICreateBoundedSurface Method (IBody2)

Creates a bounded surface from an independent base surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateBoundedSurface( _
   ByVal UOpt As System.Boolean, _
   ByVal VOpt As System.Boolean, _
   ByRef UvParams As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim UOpt As System.Boolean
Dim VOpt As System.Boolean
Dim UvParams As System.Double

instance.ICreateBoundedSurface(UOpt, VOpt, UvParams)
```

### C#

```csharp
void ICreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   ref System.double UvParams
)
```

### C++/CLI

```cpp
void ICreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   System.double% UvParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UOpt`: True if U parameter range is given in uvData, false for the entire U parameter range
- `VOpt`: True if V parameter range is given in uvData, false for the entire V parameter range
- `UvParams`: Array of 4 doubles (see **Remarks**)

## VBA Syntax

See [Body2::ICreateBoundedSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateBoundedSurface.html).

## Remarks

Before you use this method, you must call one of the base surface creation methods, such as [IBody2::ICreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBsplineSurface.html).

The UOpt and VOpt arguments allow the application to supply parameter range information so that a bounded surface can be made up from part of the base surface. If UOpt and VOpt are both set to false, then SOLIDWORKS uses the entire parameter ranges. This method fails for surfaces with infinite parameter ranges.

UvParams contains 4 doubles describing the UV parameter ranges.

| U parameter range | uvData[0] and uvData[1] ; UvData[0] must be less than uvData[1] |
| --- | --- |
| V parameter range | uvData[2] and uvData[3] ; UvData[2] must be less than uvData[3] |

To construct a solid body from bounded surfaces, call [IPartDoc::ICreateNewBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateNewBody2.html) first, which arranges for a placeholder for this bounded surface.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateBoundedSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBoundedSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
