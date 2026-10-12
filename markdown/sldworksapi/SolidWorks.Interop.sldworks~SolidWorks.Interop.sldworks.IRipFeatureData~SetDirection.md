---
title: "SetDirection Method (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "SetDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~SetDirection.html"
---

# SetDirection Method (IRipFeatureData)

Sets the direction for this rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirection( _
   ByVal Edge As System.Object, _
   ByVal Dir As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
Dim Edge As System.Object
Dim Dir As System.Integer

instance.SetDirection(Edge, Dir)
```

### C#

```csharp
void SetDirection(
   System.object Edge,
   System.int Dir
)
```

### C++/CLI

```cpp
void SetDirection(
   System.Object^ Edge,
   System.int Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Edge`: Rip feature [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
- `Dir`: Direction of rip feature:

  - 0 = this direction
  - 1 = other direction
  - 2 = both directions

## VBA Syntax

See [RipFeatureData::SetDirection](ms-its:sldworksapivb6.chm::/sldworks~RipFeatureData~SetDirection.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)
[IRipFeatureData::GetDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetDirection.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
