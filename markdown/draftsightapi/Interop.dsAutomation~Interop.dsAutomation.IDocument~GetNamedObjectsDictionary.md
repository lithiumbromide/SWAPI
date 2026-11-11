---
title: "GetNamedObjectsDictionary Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetNamedObjectsDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetNamedObjectsDictionary.html"
---

# GetNamedObjectsDictionary Method (IDocument)

Gets the named-objects dictionary for the drawing.

## Syntax

### Visual Basic

```vb
Function GetNamedObjectsDictionary() As Dictionary
```

### C#

```csharp
Dictionary GetNamedObjectsDictionary()
```

### JScript

```
function GetNamedObjectsDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* GetNamedObjectsDictionary();
```

### C++/CLI

```cpp
Dictionary^ GetNamedObjectsDictionary();
```

### Return Value

[Named-objects dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

A named-objects dictionary for a drawing associates unique entry names with unique objects of any type.

The named-objects dictionary is the root dictionary of non-graphical objects in the drawing.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R4.0
