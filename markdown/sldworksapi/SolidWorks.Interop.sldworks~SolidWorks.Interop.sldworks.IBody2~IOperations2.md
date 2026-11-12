---
title: "IOperations2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IOperations2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.html"
---

# IOperations2 Method (IBody2)

Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function IOperations2( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body2, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As Body2
Dim ErrorCode As System.Integer
Dim value As EnumBodies2

value = instance.IOperations2(OperationType, ToolBody, ErrorCode)
```

### C#

```csharp
EnumBodies2 IOperations2(
   System.int OperationType,
   Body2 ToolBody,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
EnumBodies2^ IOperations2(
   System.int OperationType,
   Body2^ ToolBody,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`: Operation type as defined in [swBodyOperationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyOperationType_e.html)
- `ToolBody`: Pointer to the tool [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `ErrorCode`: Error indicator as defined in [swBodyOperationError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationError_e.html); returns swBodyOperationNoError if SOLIDWORKS does not generate an error

### Return Value

Resulting [bodies enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [Body2::IOperations2](ms-its:sldworksapivb6.chm::/sldworks~Body2~IOperations2.html).

## Remarks

If the target and tool bodies are the same in geometry, the result body of this method is NULL, and the return value is S_false.

This method works with two temporary bodies; one is the target and one is the tool. The output is a list of bodies resulting from the operation.

The two temporary bodies used in this function (the Body2 and ToolBody pointers) are invalid once the operation is complete. COM applications should release these two pointers after using this method. If your application needs to maintain these bodies, then you should make a copy of them using [IBody2::ICopy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICopy.html) before passing them to this routine.

To perform a [swBodyOperationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyOperationType_e.html).SWBODYINTERSECT between a sheet (surface) and a solid body, the sheet body must be the target body.

Use [IBody2::Check3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Check3.html) for both bodies before using this method to ensure that both bodies are valid solids. Using this method with invalid bodies can cause unexpected results.

If a non-manifold error is returned, use [IBody2::ResetEdgeTolerances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ResetEdgeTolerances.html) to visit all of the edges in the body to reset their tolerances. Then use IBody2::Operations2 again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::Operations2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
