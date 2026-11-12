---
title: "SaveToFile2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SaveToFile2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SaveToFile2.html"
---

# SaveToFile2 Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::SaveToFile3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SaveToFile3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveToFile2( _
   ByVal Name As System.String, _
   ByVal Options As System.Integer, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Name As System.String
Dim Options As System.Integer
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean

value = instance.SaveToFile2(Name, Options, Errors, Warnings)
```

### C#

```csharp
System.bool SaveToFile2(
   System.string Name,
   System.int Options,
   out System.int Errors,
   out System.int Warnings
)
```

### C++/CLI

```cpp
System.bool SaveToFile2(
   System.String^ Name,
   System.int Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the part document (.sldprt)
- `Options`: Relevant options indicating how to save the document as defined in [swSaveAsOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html)
- `Errors`: Errors that caused the save to fail as defined in [swFileSaveError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)
- `Warnings`: Warnings or extra information generated during the save operation as defined in [swFileSaveWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html)

### Return Value

True if the save is successful, false if not

## VBA Syntax

See [PartDoc::SaveToFile2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SaveToFile2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
