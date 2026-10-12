---
title: "GetUseDocTextFormat Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetUseDocTextFormat.html"
---

# GetUseDocTextFormat Method (IDrSection)

Gets whether SOLIDWORKS is currently using the document default setting for text format.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocTextFormat() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetUseDocTextFormat()
```

### C#

```csharp
System.bool GetUseDocTextFormat()
```

### C++/CLI

```cpp
System.bool GetUseDocTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if using the document default setting for text format, false if not

## VBA Syntax

See [DrSection::GetUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetUseDocTextFormat.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextFormat.html)
[IDrSection::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextFormat.html)
[IDrSection::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetTextFormat.html)
[IDrSection::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetTextFormat.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
