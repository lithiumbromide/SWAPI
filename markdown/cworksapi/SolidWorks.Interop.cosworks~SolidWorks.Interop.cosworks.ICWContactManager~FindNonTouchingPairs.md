---
title: "FindNonTouchingPairs Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "FindNonTouchingPairs"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindNonTouchingPairs.html"
---

# FindNonTouchingPairs Method (ICWContactManager)

Finds non-touching faces within the specified minimum and maximum distance in the specified bodies or components.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindNonTouchingPairs( _
   ByVal VarCompBodies As System.Object, _
   ByVal DMin As System.Double, _
   ByVal DMax As System.Double, _
   ByRef NEnts As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim VarCompBodies As System.Object
Dim DMin As System.Double
Dim DMax As System.Double
Dim NEnts As System.Integer
Dim value As System.Object

value = instance.FindNonTouchingPairs(VarCompBodies, DMin, DMax, NEnts)
```

### C#

```csharp
System.object FindNonTouchingPairs(
   System.object VarCompBodies,
   System.double DMin,
   System.double DMax,
   out System.int NEnts
)
```

### C++/CLI

```cpp
System.Object^ FindNonTouchingPairs(
   System.Object^ VarCompBodies,
   System.double DMin,
   System.double DMax,
   [Out] System.int NEnts
)
```

### Parameters

- `VarCompBodies`: Array of bodies or components
- `DMin`: Minimum clearance; face pairs closer than this distance do not appear in the returned array
- `DMax`: Maximum clearance; face pairs further apart than this distance do not appear in the returned array
- `NEnts`: Number of non-touching faces

### Return Value

Array of non-touching face pairs

## VBA Syntax

See [CWContactManager::FindNonTouchingPairs](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~FindNonTouchingPairs.html).

## Remarks

nEnts contains the size of the returned array. The returned array contains consecutive pairs of non-touching faces.

To create contact sets using the returned array, call [ICWContactManager::CreateContactSetsFromPairList](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html).

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::FindTouchingEdgeFacePairs Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingEdgeFacePairs.html)
[ICWContactManager::FindTouchingFacePairs Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingFacePairs.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
