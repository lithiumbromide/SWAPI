---
title: "mbsPicturePath Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserDataEx"
member: "mbsPicturePath"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx~mbsPicturePath.html"
---

# mbsPicturePath Field

Points to an image file (e.g., **.jpg**, **.bmp**, **.png**, etc.) that can be set using [IEdmUser10::SetUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~SetUserDataEx.html).

## Syntax

### Visual Basic

```vb
Public mbsPicturePath As System.String
```

### C#

```csharp
public System.string mbsPicturePath
```

### C++/CLI

```cpp
public:
System.String^ mbsPicturePath
```

## Remarks

The member can be set to an empty or null string to remove the user's picture.

If you call [IEdmUser10::GetUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~GetUserDataEx.html), then this field points to the user's picture cached to the client computer disk. This is the cache used bySOLIDWORKS PDM Professional, so you should not delete the file from that location.

## See Also

[EdmUserDataEx Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx.html)
[EdmUserDataEx Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx_members.html)
