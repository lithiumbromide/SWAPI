---
title: "GetBendState Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetBendState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBendState.html"
---

# GetBendState Method (IModelDoc2)

Gets the current bend state of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendState() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetBendState()
```

### C#

```csharp
System.int GetBendState()
```

### C++/CLI

```cpp
System.int GetBendState();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current state of sheet metal bends as defined in [swSMBendState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html)

## VBA Syntax

See [ModelDoc2::GetBendState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetBendState.html).

## Examples

[Flatten Sheet Metal Part (VBA)](Flatten_Sheet_Metal_Part_Example_VB.htm)

## Remarks

| If... | Then... |
| --- | --- |
| A part with bend information is being edited in context of the assembly (see IAssemblyDoc::EditPart2 ) | The bend state for that part is returned. |
| This method is run on a part without bend information or directly on an assembly | swSMBendStateNone is returned, and the return status is S_false (COM only). |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetBendState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBendState.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
