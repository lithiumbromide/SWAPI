---
title: "PromptText Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "PromptText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PromptText.html"
---

# PromptText Property (INote)

Gets and sets the message prompt text.

## Syntax

### Visual Basic (Declaration)

```vb
Property PromptText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.String

instance.PromptText = value

value = instance.PromptText
```

### C#

```csharp
System.string PromptText {get; set;}
```

### C++/CLI

```cpp
property System.String^ PromptText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text to use in prompt message

## VBA Syntax

See [Note::PromptText](ms-its:sldworksapivb6.chm::/sldworks~Note~PromptText.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
