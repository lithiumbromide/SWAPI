---
title: "GetOpenDocSpec Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetOpenDocSpec"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocSpec.html"
---

# GetOpenDocSpec Method (ISldWorks)

Gets the specifications to use when opening a model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOpenDocSpec( _
   ByVal FileName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object

value = instance.GetOpenDocSpec(FileName)
```

### C#

```csharp
System.object GetOpenDocSpec(
   System.string FileName
)
```

### C++/CLI

```cpp
System.Object^ GetOpenDocSpec(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name of the document to open

### Return Value

[Document specification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification.html)

## VBA Syntax

See [SldWorks::GetOpenDocSpec](ms-its:sldworksapivb6.chm::/Sldworks~SldWorks~GetOpenDocSpec.html).

## Examples

[Hide All Edges in Drawing View (VBA)](Hide_All_Edges_in_Drawing_View_Example_VB.htm)
[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
