---
title: "SetReferencePlane Method (ICWMaterial)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMaterial"
member: "SetReferencePlane"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~SetReferencePlane.html"
---

# SetReferencePlane Method (ICWMaterial)

Sets the name of the reference plane or reference axis used to specify material properties for orthotropic materials.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferencePlane( _
   ByVal PlaneDisp As System.Object, _
   ByRef ErrorCode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMaterial
Dim PlaneDisp As System.Object
Dim ErrorCode As System.Integer

instance.SetReferencePlane(PlaneDisp, ErrorCode)
```

### C#

```csharp
void SetReferencePlane(
   System.object PlaneDisp,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
void SetReferencePlane(
   System.Object^ PlaneDisp,
   [Out] System.int ErrorCode
)
```

### Parameters

- `PlaneDisp`: Reference entity
- `ErrorCode`: Error as defined in [swsMaterialReferencePlaneError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialReferencePlaneError_e.html)

## VBA Syntax

See [CWMaterial::SetReferencePlane](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMaterial~SetReferencePlane.html).

## See Also

[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWMaterial Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial_members.html)
[ICWMaterial::GetReferencePlaneName Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial~GetReferencePlaneName.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
