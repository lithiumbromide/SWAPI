---
title: "LockPath Property (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "LockPath"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~LockPath.html"
---

# LockPath Property (IEdmReference5)

Gets the file's check-out path.

## Syntax

### Visual Basic

```vb
ReadOnly Property LockPath As System.String
```

### C#

```csharp
System.string LockPath {get;}
```

### C++/CLI

```cpp
property System.String^ LockPath {
   System.String^ get();
}
```

## Remarks

The retrun value is empty if the file is not checked out.

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
