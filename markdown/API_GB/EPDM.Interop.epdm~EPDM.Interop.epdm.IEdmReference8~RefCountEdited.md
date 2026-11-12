---
title: "RefCountEdited Property (IEdmReference8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference8"
member: "RefCountEdited"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8~RefCountEdited.html"
---

# RefCountEdited Property (IEdmReference8)

Gets or sets the reference count used in bills of materials.

## Syntax

### Visual Basic

```vb
Property RefCountEdited As System.Integer
```

### C#

```csharp
System.int RefCountEdited {get; set;}
```

### C++/CLI

```cpp
property System.int RefCountEdited {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Reference count used in bills of materials

## Remarks

A value of -1 is returned if the reference count has not been edited.

## See Also

[IEdmReference8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8.html)
[IEdmReference8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8_members.html)
[IEdmReference6::RefCount Property ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6~RefCount.html)

## Availability

SOLIDWORKS PDM Professional 2011
