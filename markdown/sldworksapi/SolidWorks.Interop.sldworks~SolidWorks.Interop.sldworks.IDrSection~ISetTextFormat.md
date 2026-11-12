---
title: "ISetTextFormat Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "ISetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetTextFormat.html"
---

# ISetTextFormat Method (IDrSection)

Sets the text format for the text for this section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean

value = instance.ISetTextFormat(UseDoc, TextFormat)
```

### C#

```csharp
System.bool ISetTextFormat(
   System.bool UseDoc,
   TextFormat TextFormat
)
```

### C++/CLI

```cpp
System.bool ISetTextFormat(
   System.bool UseDoc,
   TextFormat^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True if set to use the appropriate document default setting, false if it is not (see **Remarks**)
- `TextFormat`: Pointer to the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object for this section line text

### Return Value

True if text format is successfully set, false if not

## VBA Syntax

See [DrSection::ISetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DrSection~ISetTextFormat.html).

## Remarks

If UseDoc is True, then use the appropriate document default setting. SOLIDWORKS will also ignore TextFormat, which you should set to NULL.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetTextFormat.html)
[IDrSection::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextFormat.html)
[IDrSection::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextFormat.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
