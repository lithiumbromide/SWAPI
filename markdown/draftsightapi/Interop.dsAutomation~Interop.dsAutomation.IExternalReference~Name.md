---
title: "Name Property (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "Name"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~Name.html"
---

# Name Property (IExternalReference)

Gets or sets the name of the external reference.

## Syntax

### Visual Basic

```vb
Property Name As System.String
```

### C#

```csharp
System.string Name {get; set;}
```

### JScript

```
function get,set Name : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Name();
__property void set_Name(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the external reference

## Examples

This code snippet shows how to get the external references and their names and paths.

##### COM native C++

_variant_t pVariantArray = dsDoc->GetExternalReferences();
if( V_VT( &pVariantArray ) != VT_EMPTY )
{
IExternalReferencePtr *ExtRef = NULL;
int countOfExtRef = 0;
[TypeConverter::convertVariantArrayToPtrArray](GettingStarted-draftsightapi.html#convertVariantArrayToPtrArray)<IExternalReferencePtr, IExternalReference>( pVariantArray, ExtRef, countOfExtRef );

if( ExtRef && countOfExtRef > 0)
{
for( int i = 0; i < countOfExtRef; ++i )
{
bstr_t blockName= ExtRef[i]->GetName();

bstr_t xRefPath = ExtRef[i]->GetPathName();

}
delete[] ExtRef;
}
}

## Examples

[Insert External Reference (C#)](Insert_External_Reference_Example_CSharp.htm)
[Insert External Reference (VB.NET)](Insert_External_Reference_Example_VBNET.htm)
[Insert External Reference (VBA)](Insert_External_Reference_Example_VBA.htm)

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)
[IExternalReference::PathName Property](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~PathName.html)

## Availability

DraftSight V1R1
