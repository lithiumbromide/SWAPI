---
title: "GetMenuStrings Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMenuStrings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.html"
---

# GetMenuStrings Method (ISldWorks)

Gets the name of the parent menu of the specified menu command.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMenuStrings( _
   ByVal CommandID As System.Integer, _
   ByVal DocumentType As System.Integer, _
   ByRef ParentMenuName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim DocumentType As System.Integer
Dim ParentMenuName As System.String
Dim value As System.String

value = instance.GetMenuStrings(CommandID, DocumentType, ParentMenuName)
```

### C#

```csharp
System.string GetMenuStrings(
   System.int CommandID,
   System.int DocumentType,
   out System.string ParentMenuName
)
```

### C++/CLI

```cpp
System.String^ GetMenuStrings(
   System.int CommandID,
   System.int DocumentType,
   [Out] System.String^ ParentMenuName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: Command ID of the command whose parent menu's name you want
- `DocumentType`: Document types in which this command exists as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `ParentMenuName`: Name of the parent menu of the specified menu command

### Return Value

Menu string

## VBA Syntax

See [SldWorks::GetMenuStrings](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMenuStrings.html).

## Remarks

Use this method with methods that require you to supply the name of the menu, such as [ISldWorks::RemoveMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveMenu.html), [IFrame::RenameMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~RenameMenu.html) and [IFrame::RemoveMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~RemoveMenu.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
