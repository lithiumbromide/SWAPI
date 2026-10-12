---
title: "InsertJoin2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertJoin2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertJoin2.html"
---

# InsertJoin2 Method (IAssemblyDoc)

Constructs a feature from merged selected components.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertJoin2( _
   ByVal HideParts As System.Boolean, _
   ByVal ForceContact As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim HideParts As System.Boolean
Dim ForceContact As System.Boolean
Dim value As System.Boolean

value = instance.InsertJoin2(HideParts, ForceContact)
```

### C#

```csharp
System.bool InsertJoin2(
   System.bool HideParts,
   System.bool ForceContact
)
```

### C++/CLI

```cpp
System.bool InsertJoin2(
   System.bool HideParts,
   System.bool ForceContact
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HideParts`: True hides the original components after the join is complete, false shows them
- `ForceContact`: True joins any coincident faces and intruding volumes, false does not

### Return Value

True if feature creation was successful, false if it was not

## VBA Syntax

See [AssemblyDoc::InsertJoin2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertJoin2.html).

## Examples

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

## Remarks

When you use this method, SOLIDWORKS must be in Edit Part mode for the target part. You must also preselect the component parts to be merged into the edited part.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
