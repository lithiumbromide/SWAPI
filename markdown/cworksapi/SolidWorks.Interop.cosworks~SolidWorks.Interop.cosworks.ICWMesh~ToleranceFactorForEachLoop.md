---
title: "ToleranceFactorForEachLoop Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "ToleranceFactorForEachLoop"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ToleranceFactorForEachLoop.html"
---

# ToleranceFactorForEachLoop Property (ICWMesh)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceFactorForEachLoop As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Double

instance.ToleranceFactorForEachLoop = value

value = instance.ToleranceFactorForEachLoop
```

### C#

```csharp
System.double ToleranceFactorForEachLoop {get; set;}
```

### C++/CLI

```cpp
property System.double ToleranceFactorForEachLoop {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Tolerance factor for mesh loops

## VBA Syntax

See [CWMesh::ToleranceFactorForEachLoop](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~ToleranceFactorForEachLoop.html).

## Remarks

The tolerance factor for each is the factor by which the new global element size if multipled to calculate the new global element size.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::AutomaticLooping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticLooping.html)
[ICWMesh::NumberOfLoops Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NumberOfLoops.html)
[ICWMesh::GetDefaultElementSizeAndTolerance Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
