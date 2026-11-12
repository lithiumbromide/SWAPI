---
title: "AddPrefix Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "AddPrefix"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddPrefix.html"
---

# AddPrefix Property (IPackAndGo)

Gets or sets a prefix for all filenames for Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Property AddPrefix As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.String

instance.AddPrefix = value

value = instance.AddPrefix
```

### C#

```csharp
System.string AddPrefix {get; set;}
```

### C++/CLI

```cpp
property System.String^ AddPrefix {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Prefix for all filenames

## VBA Syntax

See [PackAndGo::AddPrefix](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~AddPrefix.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::AddSuffix Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddSuffix.html)
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)
[IPackAndGo::SetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html)
[IPackAndGo::SetSaveToName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
