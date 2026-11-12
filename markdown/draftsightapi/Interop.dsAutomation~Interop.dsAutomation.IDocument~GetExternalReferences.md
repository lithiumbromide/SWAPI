---
title: "GetExternalReferences Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetExternalReferences"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetExternalReferences.html"
---

# GetExternalReferences Method (IDocument)

Gets all external references for this document.

## Syntax

### Visual Basic

```vb
Function GetExternalReferences() As System.Object
```

### C#

```csharp
System.object GetExternalReferences()
```

### JScript

```
function GetExternalReferences() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetExternalReferences();
```

### C++/CLI

```cpp
System.Object^ GetExternalReferences();
```

### Return Value

Array of [external references](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)

## Examples

This code snippet shows how to get the document's external references.

##### COM native C++

_variant_t pVariantArray = dsDoc->GetExternalReferences();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{

. . .

}

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetImmediateChildReferences Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetImmediateChildReferences.html)

## Availability

DraftSight V1R1
