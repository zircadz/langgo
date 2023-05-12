import * as React from 'react';
import { PrimaryButton } from '@workday/canvas-kit-react';
import { Card } from '@workday/canvas-kit-react/card';
import { Flex } from '@workday/canvas-kit-react/layout';

import './App.css';

const baseStyles = {
  color: 'white',
  minHeight: 'xl',
  minWidth: '2rem',
  padding: 'xs',
};

function App() {
  return (
    <div className="App">
      <h1>Langgo</h1>
      <PrimaryButton>Home</PrimaryButton>
      <div>
        <Flex columnGap="xs">
          <Flex flexDirection="column" rowGap="xs" flex={1}>
            <Flex.Item backgroundColor="white" textAlign="center" {...baseStyles}>
              <Card depth={2} padding="xs">
                <Card.Heading>Language #1</Card.Heading>
                <Card.Body>
                  Language Translation
                </Card.Body>
              </Card>
            </Flex.Item>
          </Flex>
          <Flex flexDirection="column" rowGap="xs" flex={2}>
            <Flex.Item backgroundColor="white" textAlign="center" {...baseStyles}>
              <Card depth={2} padding="xs">
                <Card.Heading>Language #2</Card.Heading>
                <Card.Body>
                  Language Translation
                </Card.Body>
              </Card>
            </Flex.Item>
          </Flex>
          <Flex flexDirection="column" rowGap="xs" flex={1}>
            <Flex.Item backgroundColor="white" textAlign="center" {...baseStyles}>
              <Card depth={2} padding="xs">
                <Card.Heading>Language #3</Card.Heading>
                <Card.Body>
                  Language Translation
                </Card.Body>
              </Card>
            </Flex.Item>
          </Flex>
        </Flex>
      </div>
    </div>
  );
}

export default App;
