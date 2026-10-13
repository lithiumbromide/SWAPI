---
title: "IsOpenedViewOnly Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsOpenedViewOnly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.html"
---

# IsOpenedViewOnly Method (IModelDoc2)

Gets whether a SOLIDWORKS document is open in view-only mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsOpenedViewOnly() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.IsOpenedViewOnly()
```

### C#

```csharp
System.bool IsOpenedViewOnly()
```

### C++/CLI

```cpp
System.bool IsOpenedViewOnly();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if document is in a view-only state, false if not

## VBA Syntax

See [ModelDoc2::IsOpenedViewOnly](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsOpenedViewOnly.html).

## Remarks

Files are loaded using multi-threading. When a file is loading, the graphics are displayed immediately and the end-user is able to perform certain view zooming and panning functions. Until all data and references are loaded, the file is in view-only mode.

A file can be in view-only mode if the end-user chose to load the file for viewing purposes. You application should check for view-only mode to determine how to proceed.

NOTE: When a file is in view-only mode, many API queries return NULL or empty data.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IsOpenedReadOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedReadOnly.html)
[IModelDoc2::SetReadOnlyState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetReadOnlyState.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
