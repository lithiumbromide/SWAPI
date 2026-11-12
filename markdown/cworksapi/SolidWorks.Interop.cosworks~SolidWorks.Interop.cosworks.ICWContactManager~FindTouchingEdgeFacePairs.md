---
title: "FindTouchingEdgeFacePairs Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "FindTouchingEdgeFacePairs"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingEdgeFacePairs.html"
---

# FindTouchingEdgeFacePairs Method (ICWContactManager)

Finds touching shell edges and faces in the specified bodies or components.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindTouchingEdgeFacePairs( _
   ByVal VarCompBodies As System.Object, _
   ByRef NEdgeFaces As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim VarCompBodies As System.Object
Dim NEdgeFaces As System.Integer
Dim value As System.Object

value = instance.FindTouchingEdgeFacePairs(VarCompBodies, NEdgeFaces)
```

### C#

```csharp
System.object FindTouchingEdgeFacePairs(
   System.object VarCompBodies,
   out System.int NEdgeFaces
)
```

### C++/CLI

```cpp
System.Object^ FindTouchingEdgeFacePairs(
   System.Object^ VarCompBodies,
   [Out] System.int NEdgeFaces
)
```

### Parameters

- `VarCompBodies`: Array of bodies or components
- `NEdgeFaces`: Number of touching shell edges and faces

### Return Value

Array of touching shell edge and face pairs

## VBA Syntax

See [CWContactManager::FindTouchingEdgeFacePairs](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~FindTouchingEdgeFacePairs.html).

## Remarks

NEdgeFaces contains the size of the returned array. The returned array contains consecutive pairs of touching entities.

To create contact sets using the returned array, call [ICWContactManager::CreateContactSetsFromPairList](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html).

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::FindNonTouchingPairs Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindNonTouchingPairs.html)
[ICWContactManager::FindTouchingFacePairs Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingFacePairs.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
