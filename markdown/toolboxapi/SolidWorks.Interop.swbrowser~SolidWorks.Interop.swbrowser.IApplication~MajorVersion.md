---
title: "MajorVersion Property (IApplication)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IApplication"
member: "MajorVersion"
kind: "property"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication~MajorVersion.html"
---

# MajorVersion Property (IApplication)

Gets the major version of the SOLIDWORKS Toolbox Browser add-in.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MajorVersion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IApplication
Dim value As System.Integer

value = instance.MajorVersion
```

### C#

```csharp
System.int MajorVersion {get;}
```

### C++/CLI

```cpp
property System.int MajorVersion {
   System.int get();
}
```

### Property Value

Major version of the SOLIDWORKS Toolbox Browser add-in

## VBA Syntax

See [Application::MajorVersion](ms-its:toolboxapivb6.chm::/ToolboxBrowser~Application~MajorVersion.html).

## See Also

[IApplication Interface](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication.html)
[IApplication Members](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IApplication_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
