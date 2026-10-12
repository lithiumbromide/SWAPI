---
title: "CreateBoundedSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateBoundedSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBoundedSurface.html"
---

# CreateBoundedSurface Method (IBody2)

Creates a bounded surface from an independent base surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBoundedSurface( _
   ByVal UOpt As System.Boolean, _
   ByVal VOpt As System.Boolean, _
   ByVal UvParams As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim UOpt As System.Boolean
Dim VOpt As System.Boolean
Dim UvParams As System.Object
Dim value As System.Boolean

value = instance.CreateBoundedSurface(UOpt, VOpt, UvParams)
```

### C#

```csharp
System.bool CreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   System.object UvParams
)
```

### C++/CLI

```cpp
System.bool CreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   System.Object^ UvParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UOpt`: True if U parameter range is given in uvData, false for the entire U parameter range
- `VOpt`: True if V parameter range is given in uvData, false for the entire V parameter range
- `UvParams`: Array of 4 doubles (see **Remarks**)

### Return Value

True if bounded surface creation was successful, false if not

## VBA Syntax

See [Body2::CreateBoundedSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateBoundedSurface.html).

## Remarks

Before you use this method, you must call one of the base surface creation methods, such as [IBody2::CreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBsplineSurface.html).

The UOpt and VOpt arguments allow the application to supply parameter range information so that a bounded surface can be made up from part of the base surface. If UOpt and VOpt are both set to false, then SOLIDWORKS uses the entire parameter ranges. This method fails for surfaces with infinite parameter ranges.

UvParams contains 4 doubles describing the UV parameter ranges.

| U parameter range | uvData[0] and uvData[1] ; UvData[0] must be less than uvData[1] |
| --- | --- |
| V parameter range | uvData[2] and uvData[3] ; UvData[2] must be less than uvData[3] |

To construct a solid body from bounded surfaces, call [IPartDoc::CreateNewBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateNewBody.html) first, which arranges for a placeholder for this bounded surface.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateBoundedSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBoundedSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
