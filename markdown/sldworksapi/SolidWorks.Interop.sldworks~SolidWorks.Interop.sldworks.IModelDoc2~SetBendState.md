---
title: "SetBendState Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetBendState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBendState.html"
---

# SetBendState Method (IModelDoc2)

Sets the bend state of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBendState( _
   ByVal BendState As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim BendState As System.Integer
Dim value As System.Integer

value = instance.SetBendState(BendState)
```

### C#

```csharp
System.int SetBendState(
   System.int BendState
)
```

### C++/CLI

```cpp
System.int SetBendState(
   System.int BendState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BendState`: Sheet metal state to set in this part as defined in [swSMBendState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html)

### Return Value

Status of the set operation as defined in [swSMCommandStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMCommandStatus_e.html) (see **Remarks**)

## VBA Syntax

See [ModelDoc2::SetBendState](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetBendState.html).

## Examples

[Flatten Sheet Metal Part (VBA)](Flatten_Sheet_Metal_Part_Example_VB.htm)

## Remarks

This method only works for old-style sheet metal parts or non-sheet metal parts converted to sheet metal parts. To set the bend state on new-style sheet metal parts (i.e., those that have a base flange as their first feature), suppress and unsuppress the flat-pattern feature.

If editing a part with bend information in the context of the assembly (see [IAssemblyDoc::EditPart2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EditPart2.html)), the bend state for that part will be set.

| If this method is executed on... | Then... |
| --- | --- |
| Part without bend information | The part is not affected, and retval is set to swSMErrorNotASheetMetalPart |
| Assembly | The assembly is not affected, and retval is set to swSMErrorNotAPart |
| NOTE: In both of these cases, status is S_false for the COM version of this method. |  |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetBendState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBendState.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
