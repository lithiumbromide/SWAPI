---
title: "RefCount Property (IEdmReference6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference6"
member: "RefCount"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6~RefCount.html"
---

# RefCount Property (IEdmReference6)

Gets the number of times the referenced file is included by the referencing file.

## Syntax

### Visual Basic

```vb
ReadOnly Property RefCount As System.Integer
```

### C#

```csharp
System.int RefCount {get;}
```

### C++/CLI

```cpp
property System.int RefCount {
   System.int get();
}
```

### Property Value

Number of times the referenced file is included by the referencing file (see **Remarks**)

## Remarks

This property is 0 if the file format does not allow SOLIDWORKS PDM Professional to access the information.

## See Also

[IEdmReference6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6.html)
[IEdmReference6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6_members.html)
[IEdmReference8::RefCountEdited Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8~RefCountEdited.html)

## Availability

Version 6.0 of SOLIDWORKS PDM Professional
