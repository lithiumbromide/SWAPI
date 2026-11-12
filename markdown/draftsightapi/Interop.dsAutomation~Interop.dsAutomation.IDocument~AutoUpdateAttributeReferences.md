---
title: "AutoUpdateAttributeReferences Property (IDocument)"
project: ""
interface: "IDocument"
member: "AutoUpdateAttributeReferences"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~AutoUpdateAttributeReferences.html"
---

# AutoUpdateAttributeReferences Property (IDocument)

Gets or sets whether to update all existing block attribute references in the document with changes.

## Syntax

### Visual Basic

```vb
Property AutoUpdateAttributeReferences As System.Boolean
```

### C#

```csharp
System.bool AutoUpdateAttributeReferences {get; set;}
```

### JScript

```
function get,set AutoUpdateAttributeReferences : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_AutoUpdateAttributeReferences();
__property void set_AutoUpdateAttributeReferences(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool AutoUpdateAttributeReferences {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to update all existing block attribute references in the document with changes, false to not

## Remarks

This property corresponds to the **Apply changes to existing references** option in the Block Attribute Manager dialog.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight 2023 SP0
