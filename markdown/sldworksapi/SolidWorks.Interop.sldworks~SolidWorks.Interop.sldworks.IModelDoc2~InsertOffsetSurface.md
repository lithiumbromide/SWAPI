---
title: "InsertOffsetSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertOffsetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertOffsetSurface.html"
---

# InsertOffsetSurface Method (IModelDoc2)

Inserts an offset surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertOffsetSurface( _
   ByVal Thickness As System.Double, _
   ByVal Reverse As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Reverse As System.Boolean

instance.InsertOffsetSurface(Thickness, Reverse)
```

### C#

```csharp
void InsertOffsetSurface(
   System.double Thickness,
   System.bool Reverse
)
```

### C++/CLI

```cpp
void InsertOffsetSurface(
   System.double Thickness,
   System.bool Reverse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Offset of surface from reference
- `Reverse`: True to reverse the direction of the offset, false to not

## VBA Syntax

See [ModelDoc2::InsertOffsetSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertOffsetSurface.html).

## Remarks

Make the selections using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) before calling this method.

See the SOLIDWORKS Help for more information about what entities are valid for selection.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[IBody2::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.html)
[IBody2::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.html)
[IBody2::MakeOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MakeOffset.html)
[IModeler::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.html)
[IModeler::ICreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.html)
[ISurface::GetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetOffsetSurfParams2.html)
[ISurface::IGetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetOffsetSurfParams2.html)
[ISurface::IsOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsOffset.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
