---
title: "GetSaveToName Method (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "GetSaveToName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetSaveToName.html"
---

# GetSaveToName Method (IPackAndGo)

Gets the path or the path and filename of the Zip file for Pack and Go set by [IPackAndGo::SetSaveToName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo~SetSaveToName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSaveToName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.String

value = instance.GetSaveToName()
```

### C#

```csharp
System.string GetSaveToName()
```

### C++/CLI

```cpp
System.String^ GetSaveToName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Path or the path and filename of the Zip file set by IPackAndGo::SetSaveToName

## VBA Syntax

See [PackAndGo::GetSaveToName](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~GetSaveToName.html).

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::GetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.html)
[IPackAndGo::IGetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
