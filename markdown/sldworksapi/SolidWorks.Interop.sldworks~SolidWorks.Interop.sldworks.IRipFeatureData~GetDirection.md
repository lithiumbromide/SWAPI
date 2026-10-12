---
title: "GetDirection Method (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "GetDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetDirection.html"
---

# GetDirection Method (IRipFeatureData)

Gets the rip direction for the specified edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDirection( _
   ByVal Edge As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
Dim Edge As System.Object
Dim value As System.Integer

value = instance.GetDirection(Edge)
```

### C#

```csharp
System.int GetDirection(
   System.object Edge
)
```

### C++/CLI

```cpp
System.int GetDirection(
   System.Object^ Edge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Edge`: [Edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

### Return Value

Direction of the rip feature for the specified edge:

- 0 = this direction
- 1 = other direction
- 2 = both directions

## VBA Syntax

See [RipFeatureData::GetDirection](ms-its:sldworksapivb6.chm::/sldworks~RipFeatureData~GetDirection.html).

## Examples

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)
[IRipFeatureData::SetDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~SetDirection.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
