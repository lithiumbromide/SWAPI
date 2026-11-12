---
title: "IsFutureVersion Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsFutureVersion"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsFutureVersion.html"
---

# IsFutureVersion Method (IModelDocExtension)

Gets whether this document is for a future version of SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsFutureVersion() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.IsFutureVersion()
```

### C#

```csharp
System.bool IsFutureVersion()
```

### C++/CLI

```cpp
System.bool IsFutureVersion();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the document is for a future version of SOLIDWORKS, false if not

## VBA Syntax

See [ModelDocExtension::IsFutureVersion](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsFutureVersion.html).

## Examples

[Get Version History of Future Version Document (VBA)](Get_Version_History_of_Future_Version_Document_Example_VB.htm)
[Get Version History of Future Version Document (VB.NET)](Get_Version_History_of_Future_Version_Document_Example_VBNET.htm)
[Get Version History of Future Version Document (C#)](Get_Version_History_of_Future_Version_Document_Example_CSharp.htm)

## Remarks

As of 2012 SP5, loading future file versions is supported, and [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) no longer throws a [swFileLoadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).swFutureVersion error.

Use IModelDocExtension::IsFutureVersion to determine:

- how to obtain the correct version history of a document. If a future version document is loaded in an older version of SOLIDWORKS, [IModelDoc2::VersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~VersionHistory.html) and [IModelDoc2::IVersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IVersionHistory.html) return the version history of the part template, not the version history of the future version document. To get the version history of a future version document, use [ISldWorks::VersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~VersionHistory.html) or [ISldWorks::IVersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IVersionHistory.html) to get the version history from its file.
- whether a component is for a future version of SOLIDWORKS and should be hidden in the user interface of older versions. Although they can be loaded, future version components may not be actionable in older versions of SOLIDWORKS.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2012 SP5, Revision Number 20.5
