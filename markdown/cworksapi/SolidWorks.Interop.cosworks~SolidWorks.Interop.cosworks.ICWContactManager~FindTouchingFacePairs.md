---
title: "FindTouchingFacePairs Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "FindTouchingFacePairs"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingFacePairs.html"
---

# FindTouchingFacePairs Method (ICWContactManager)

Finds touching faces in the specified bodies or components.

## Syntax

### Visual Basic (Declaration)

```vb
Function FindTouchingFacePairs( _
   ByVal VarCompBodies As System.Object, _
   ByRef NFaces As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim VarCompBodies As System.Object
Dim NFaces As System.Integer
Dim value As System.Object

value = instance.FindTouchingFacePairs(VarCompBodies, NFaces)
```

### C#

```csharp
System.object FindTouchingFacePairs(
   System.object VarCompBodies,
   out System.int NFaces
)
```

### C++/CLI

```cpp
System.Object^ FindTouchingFacePairs(
   System.Object^ VarCompBodies,
   [Out] System.int NFaces
)
```

### Parameters

- `VarCompBodies`: Array of bodies or components
- `NFaces`: Number of touching faces

### Return Value

Array of touching face pairs

## VBA Syntax

See [CWContactManager::FindTouchingFacePairs](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~FindTouchingFacePairs.html).

## Remarks

NFaces contains the size of the returned array. The returned array contains consecutive pairs of touching faces.

To create contact sets using the returned array, call [ICWContactManager::CreateContactSetsFromPairList](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html).

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::FindNonTouchingPairs Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindNonTouchingPairs.html)
[ICWContactManager::FindTouchingEdgeFacePairs Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~FindTouchingEdgeFacePairs.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
