---
title: "SetBody Method (IImportedCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IImportedCurveFeatureData"
member: "SetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~SetBody.html"
---

# SetBody Method (IImportedCurveFeatureData)

Modifies the wire body for this imported curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBody( _
   ByVal DispBody As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IImportedCurveFeatureData
Dim DispBody As Body2

instance.SetBody(DispBody)
```

### C#

```csharp
void SetBody(
   Body2 DispBody
)
```

### C++/CLI

```cpp
void SetBody(
   Body2^ DispBody
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispBody`: Wire [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [ImportedCurveFeatureData::SetBody](ms-its:sldworksapivb6.chm::/sldworks~ImportedCurveFeatureData~SetBody.html).

## Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, form shells.

The following methods create wire bodies:

- [IEdge::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~CreateWireBody.html)
- [ICurve::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateWireBody.html)
- [IModeler::CreateWireBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateWireBody.html)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.html)
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
