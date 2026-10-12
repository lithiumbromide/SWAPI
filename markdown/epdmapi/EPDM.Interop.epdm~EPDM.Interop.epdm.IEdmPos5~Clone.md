---
title: "Clone Method (IEdmPos5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmPos5"
member: "Clone"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~Clone.html"
---

# Clone Method (IEdmPos5)

Creates a copy of an IEdmPos5 object.

## Syntax

### Visual Basic

```vb
Function Clone() As IEdmPos5
```

### C#

```csharp
IEdmPos5 Clone()
```

### C++/CLI

```cpp
IEdmPos5^ Clone();
```

### Return Value

Copy of an [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) object

## Remarks

C++ users must release the returned pointer.

You can use a copy of an IEdmPos5 object as a bookmark in an enumeration that you are performing with this object.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmPos5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html)
[IEdmPos5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
