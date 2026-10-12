---
title: "GetDocumentNames Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "GetDocumentNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.html"
---

# GetDocumentNames Method (IPackAndGo)

Gets the original paths and filenames of all of the model's documents for Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentNames( _
   ByRef DocumentNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean

value = instance.GetDocumentNames(DocumentNames)
```

### C#

```csharp
System.bool GetDocumentNames(
   out System.object DocumentNames
)
```

### C++/CLI

```cpp
System.bool GetDocumentNames(
   [Out] System.Object^ DocumentNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentNames`: Array of strings of the original paths and filenames of all of the model's documents

### Return Value

True if the original paths and filenames of all of the model's documents are returned, false if not

## VBA Syntax

See [PackAndGo::GetDocumentNames](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~GetDocumentNames.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## Remarks

To get the drawing documents of the model, set [IPackAndGo::IncludeDrawings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~IncludeDrawings.html) to true; otherwise, the paths and filenames of the model's drawing documents are not returned.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::GetDocumentNamesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.html)
[IPackAndGo::IGetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
