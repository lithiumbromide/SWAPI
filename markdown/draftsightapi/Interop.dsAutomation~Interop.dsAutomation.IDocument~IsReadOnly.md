---
title: "IsReadOnly Method (IDocument)"
project: ""
interface: "IDocument"
member: "IsReadOnly"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~IsReadOnly.html"
---

# IsReadOnly Method (IDocument)

Gets whether the document is read only.

## Syntax

### Visual Basic

```vb
Sub IsReadOnly( _
   ByRef ReadOnly As System.Boolean _
)
```

### C#

```csharp
void IsReadOnly(
   out System.bool ReadOnly
)
```

### JScript

```
function IsReadOnly(
   ReadOnly : System.boolean
);
```

### Managed Extensions for C++

```
void IsReadOnly(
   [PARAMFLAG::Out] System.bool ReadOnly
)
```

### C++/CLI

```cpp
void IsReadOnly(
   [Out] System.bool ReadOnly
)
```

### Parameters

- `ReadOnly`: True if the document is read only, false if not

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1
