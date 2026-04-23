# 5.14.1 Security goals and threat model

5.14 Security features
5.14.1 Security goals and threat model
5.14.1.1 Overview
In many cases, the security goals and threat model used for the Internet are applicable to SCSI commands.
The Internet security goals and threat model found in RFC 3552 as they apply to SCSI are summarized in
5.14.1. Terms, concepts, and classes of security techniques that are defined in RFC 3552 are discussed
based on their RFC 3552 definitions without modification in this standard.
The security goals and threat model described in 5.14.1 are valid for all SCSI device types. Command
standards may modify this model to handle threats appropriate to specific device types.
5.14.1.2 Security goals
The overall goals of security may be divided into the following categories:
a)
communications security (i.e., protecting communications); and
b)
system security (e.g., protecting systems from unauthorized usage, inappropriate usage, and denial
of service).
These goals interact as a result of communications being carried out by systems, with access to those
systems provided through communications channels. A common methodology is to secure the communica-
tions first and then provide secure access to systems over the secured communication channels.
Communication security is subdivided into the following primary areas of protection:
a)
confidentiality: preventing unintended entities from seeing the data;
b)
cryptographic data integrity: ensuring that the data that arrives is identical to the data that was sent;
and
c)
peer entity authentication: ensuring that the communicating endpoints are the intended peer
entities.
Data origin authentication (i.e., ensuring that the received data was sent by the authenticated peer) is the
combination of peer entity authentication and cryptographic data integrity.
Non Repudiation enhances data origin authentication with the ability to prove to a third party that the sender
sent the data that the receiver received.
Cryptographic data integrity is called data integrity in RFC 3552. The term cryptographic is added in this
standard to distinguish the class of integrity protection required to counter malicious attacks from the class of
integrity protection required to deal with random data corruption (e.g., caused by cosmic rays or electrical
noise). Mechanisms used to deal with random data corruption (e.g., parity bits and CRCs) have minimal value
against malicious attacks that are able to modify integrity checks to conceal their modifications to the data.
Cryptographic data integrity requires knowledge of a secret key in order to modify an integrity check without
that modification being detectable. Systems should provide a high level of assurance that an attacker is
unable to learn, guess, discover, or otherwise obtain the required secret key.
In addition to the primary areas, there is another area of control:
a)
authorization: controlling what an entity is allowed to do. For communications security this is control
of the entities with which an entity is allowed to communicate.


A form of authorization is access control (i.e., controlling what an entity is allowed to access).
5.14.1.3 Threat model
Most secured systems are vulnerable to an attacker equipped with sufficient resources, time, and skills. In
order to make designing a security system practical, a threat model is defined to describe the capabilities that
an attacker is assumed to be able to deploy (e.g., knowledge, computing capability, and ability to control the
system).
The main purposes of a threat model are as follows:
a)
to identify the threats of concern; and
b)
to rule some threats explicitly out of scope.
Most security measures do not provide absolute assurance that an attack has not occurred. Rather, security
measures raise the difficulty of accomplishing the attack to beyond the attacker's assumed capabilities and/or
resources. Design of security measures that resist attackers with essentially unlimited capabilities (e.g.,
certain nation-states) is outside the scope of this standard. Security measures that are susceptible to a level of
capability available to some attackers may still be useful for deterring attackers who lack that level of
capability, especially when combined with non-technical security measures such as physical access controls.
The computational capability of an attacker is treated as a variable because that capability is inherently a
moving target as a result of more powerful processors. The computational capability of an attacker influences
design aspects (e.g., key length). Well designed security systems are agile in that they are able to operate not
only with different key lengths, but also with different cryptographic algorithms.
The Internet threat model described in RFC 3552 is generally applicable to SCSI, and is specifically applicable
if Internet Protocols are used by the SCSI transport (e.g., iSCSI, Fibre Channel via FCIP, or Fibre Channel via
iFCP). The basic assumptions of the Internet thread model are:
a)
end systems engaging in communication are not under the control of the attacker; and
b)
the attacker is able to read any communicated data (e.g., data in an IU) and undetectably remove,
change, or inject forged IUs, including injection of IUs that appear to be from a known and/or trusted
system.
Communications security designs are based on an additional assumption that secrets (e.g., keys) used to
secure the communications are protected so that an attacker is unable to learn, guess, discover, or otherwise
obtain them. A consequence of this assumption is that attacks against secured communications are assumed
to begin without with advance knowledge of the secrets used to secure the communications.
5.14.1.4 Types of attacks
The following types of attacks are considered:
a)
passive attacks (i.e., attacks that only require reading IUs); and
b)
active attacks (i.e., attacks that require the attacker to change communication and/or engage in
communication).
More information on attack types is available in RFC 3552.
Simple passive attacks involve reading communicated data that the attacker was not intended to see (e.g.,
password, credit card number). More complex passive attacks involve post-processing the communicated
data (e.g., checking a challenge-response pair against a dictionary to see if a common word was used as a
password).
