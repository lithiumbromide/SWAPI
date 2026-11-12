---
title: "IGetDocumentNames Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "IGetDocumentNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.html"
---

# IGetDocumentNames Method (IPackAndGo)

Gets the original paths and filenames of all of the model's documents for Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDocumentNames( _
   ByVal Count As System.Integer, _
   ByRef DocumentNames As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim Count As System.Integer
Dim DocumentNames As System.String
Dim value As System.Boolean

value = instance.IGetDocumentNames(Count, DocumentNames)
```

### C#

```csharp
System.bool IGetDocumentNames(
   System.int Count,
   out System.string DocumentNames
)
```

### C++/CLI

```cpp
System.bool IGetDocumentNames(
   System.int Count,
   [Out] System.String^ DocumentNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of model's documents
- `DocumentNames`: - in-process, unmanaged C++: Pointer to an array of strings containing the original paths and filenames of the model's documents
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the original paths and filenames of the model's documents are returned, false if not

## Remarks

Before calling this method, call [IPackAndGo::GetDocumentNamesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.html) to get the value of Count.

To get the drawing documents of the model, set [IPackAndGo::IncludeDrawings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~IncludeDrawings.html) to true; otherwise, the paths and filenames of the model's drawing documents are not returned.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::GetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
